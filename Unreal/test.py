import unreal

unreal.log_error("something mildly offensive")

#dir ()

#help(unreal.Actor.set_actor_transform)

actors = unreal.EditorLevelLibrary.get_all_level_actors()
for actor in actors:
    unreal.log (f"Actor Name:{actor.get_name()}")
    unreal.log(f"Actor Lable:{actor.get_actor_label}")
    unreal.log("---------------------")