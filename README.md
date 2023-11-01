# dconfig

This is a configuration library that exposes the functionality contained in Meta's [detectron2](https://github.com/facebookresearch/detectron2) 
and [fvcore](https://github.com/facebookresearch/fvcore) without introducing a massive amount of irrelevant dependencies.

# Installing

Use `pip`:

```
pip isntall git+https://github.com/agoryuno/dconfig
```

or add it to your `requirements.txt`:

```
https://github.com/agoryuno/dconfig
```

# Using

`dconfig` exposes the exact same `CfgNode` that `detectron2.config` does.

Look at `/dconfig/defaults.py` for an example of creating a `CfgNode` instance and populating it with values.

You can also extend an existing `CfgNode` instance object from a YAML file using `merge_from_file(filename)`, from a different `CfgNode` 
instance using `merge_from_other_cfg(cfg_other)`, or from a list with `merge_from_list(options)`.
